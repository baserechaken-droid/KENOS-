import json
import os
import subprocess
import threading

CONFIG="data/voice.json"
DEFAULT={"enabled":True,"voice":"jarvis","speed":1.15,"pitch":0.9}

class VoiceEngine:
    PROFILES={
        "jarvis":{"speed":1.15,"pitch":0.90},
        "david":{"speed":1.00,"pitch":1.00},
        "friday":{"speed":1.05,"pitch":1.20},
        "fast":{"speed":1.50,"pitch":1.00},
        "silent":{"speed":1.00,"pitch":1.00},
    }

    def __init__(self):
        self._proc=None
        self._lock=threading.Lock()
        self.settings=self._load()

    def _load(self):
        os.makedirs("data",exist_ok=True)
        if not os.path.exists(CONFIG):
            with open(CONFIG,"w") as f: json.dump(DEFAULT,f,indent=4)
            return DEFAULT.copy()
        try:
            with open(CONFIG) as f: cfg=json.load(f)
        except Exception:
            cfg=DEFAULT.copy()
        for k,v in DEFAULT.items():
            cfg.setdefault(k,v)
        return cfg

    def save(self):
        with open(CONFIG,"w") as f:
            json.dump(self.settings,f,indent=4)

    def reload(self):
        self.settings=self._load()

    def stop(self):
        with self._lock:
            if self._proc and self._proc.poll() is None:
                try: self._proc.terminate()
                except Exception: pass
            self._proc=None

    def set_voice(self,name):
        if name not in self.PROFILES: return False
        self.settings["voice"]=name
        self.settings["enabled"]=name!="silent"
        self.settings.update(self.PROFILES[name])
        self.save()
        return True

    def speak(self,text):
        if not text or not self.settings.get("enabled",True):
            return
        self.stop()
        cmd=[
            "termux-tts-speak",
            "-r",str(self.settings["speed"]),
            "-p",str(self.settings["pitch"]),
            str(text)
        ]
        try:
            with self._lock:
                self._proc=subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
        except Exception:
            pass

    def status(self):
        return dict(self.settings)

voice=VoiceEngine()
