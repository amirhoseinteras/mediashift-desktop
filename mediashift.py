"""MediaShift: offline media conversion using separately installed FFmpeg."""
from __future__ import annotations
import shutil
import subprocess
import sys
import threading
import tkinter as tk
from pathlib import Path
from tkinter import ttk,filedialog,messagebox

VERSION="1.0.0"
FORMATS=("mp4","mp3","wav","webm")

def ffmpeg_exe():
    local=Path(sys.executable if getattr(sys,"frozen",False) else __file__).resolve().parent/"ffmpeg.exe"
    return str(local) if local.is_file() else shutil.which("ffmpeg")

def unique_output(src, folder,fmt):
    candidate=folder/(src.stem+"."+fmt)
    index=1
    while candidate.exists() or candidate.resolve()==src.resolve():
        candidate=folder/(src.stem+f" ({index})."+fmt)
        index+=1
    return candidate

def command(ffmpeg,src,out,fmt):
    if fmt not in FORMATS:raise ValueError("Unsupported format.")
    if not src.is_file():raise FileNotFoundError(src)
    if src.resolve()==out.resolve():raise ValueError("Source and output must differ.")
    base=[ffmpeg,"-hide_banner","-nostdin","-y","-i",str(src)]
    if fmt=="mp3":base+=["-vn","-c:a","libmp3lame","-q:a","2"]
    elif fmt=="wav":base+=["-vn","-c:a","pcm_s16le"]
    elif fmt=="mp4":base+=["-map","0:v:0?","-map","0:a:0?","-c:v","libx264","-crf","23","-c:a","aac"]
    elif fmt=="webm":base+=["-map","0:v:0?","-map","0:a:0?","-c:v","libvpx-vp9","-crf","34","-b:v","0","-c:a","libopus"]
    return base+[str(out)]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MediaShift "+VERSION)
        self.geometry("760x300")
        self.src=tk.StringVar()
        self.dest=tk.StringVar(value=str(Path.home()/"Videos"))
        self.fmt=tk.StringVar(value="mp4")
        self.status=tk.StringVar(value="Original file stays untouched. FFmpeg required separately.")
        self.process=None
        form=ttk.Frame(self,padding=15);form.pack(fill="both",expand=True)
        for row,label,var,cb in ((0,"Input",self.src,self.choose_input),(1,"Output folder",self.dest,self.choose_folder)):
            ttk.Label(form,text=label).grid(row=row,column=0,sticky="w",pady=9)
            ttk.Entry(form,textvariable=var).grid(row=row,column=1,sticky="ew")
            ttk.Button(form,text="Browse",command=cb).grid(row=row,column=2,padx=8)
        ttk.Label(form,text="Format").grid(row=2,column=0,sticky="w",pady=9)
        ttk.Combobox(form,textvariable=self.fmt,values=FORMATS,state="readonly",width=12).grid(row=2,column=1,sticky="w")
        buttons=ttk.Frame(form);buttons.grid(row=3,column=1,sticky="w",pady=12)
        ttk.Button(buttons,text="Convert",command=self.convert).pack(side="left",padx=5)
        ttk.Button(buttons,text="Cancel",command=self.cancel).pack(side="left",padx=5)
        ttk.Label(form,textvariable=self.status,wraplength=660).grid(row=4,column=0,columnspan=3,sticky="w",pady=8)
        form.columnconfigure(1,weight=1)
    def choose_input(self):
        p=filedialog.askopenfilename()
        if p:self.src.set(p)
    def choose_folder(self):
        p=filedialog.askdirectory()
        if p:self.dest.set(p)
    def convert(self):
        if self.process and self.process.poll() is None:
            messagebox.showinfo("MediaShift","Conversion is running.");return
        ff=ffmpeg_exe()
        if not ff:
            messagebox.showerror("MediaShift","Install FFmpeg, or place ffmpeg.exe next to this app.");return
        source=Path(self.src.get());folder=Path(self.dest.get())
        if not folder.is_dir():messagebox.showerror("MediaShift","Choose an existing output folder.");return
        try:
            target=unique_output(source,folder,self.fmt.get())
            cmd=command(ff,source,target,self.fmt.get())
        except Exception as exc:messagebox.showerror("MediaShift",str(exc));return
        self.status.set("Converting...")
        def worker():
            try:
                self.process=subprocess.Popen(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,
                    creationflags=subprocess.CREATE_NO_WINDOW if sys.platform=="win32" else 0)
                _,stderr=self.process.communicate()
                if self.process.returncode:
                    if target.exists():target.unlink()
                    err=(stderr or b"")[-300:].decode("utf-8",errors="replace")
                    self.after(0,lambda:self.status.set("Conversion cancelled or failed: "+err[-160:]))
                else:self.after(0,lambda:self.status.set("Saved: "+str(target)))
            except Exception as exc:self.after(0,lambda s=str(exc):self.status.set(s))
        threading.Thread(target=worker,daemon=True).start()
    def cancel(self):
        if self.process and self.process.poll() is None:
            self.process.terminate();self.status.set("Cancelling...")
if __name__=="__main__":App().mainloop()
