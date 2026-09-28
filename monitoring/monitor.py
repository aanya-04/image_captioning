import subprocess
import threading
import time
from datetime import datetime
from statistics import mean

import psutil


class SystemMonitor:
    """
    Monitors GPU, CPU and RAM usage in a background thread.
    Samples every `interval` seconds.
    """

    def __init__(self, interval=0.5):
        self.interval = interval

        self.running = False
        self.thread = None

        self.samples = []

        self.gpu_name = None
        self.total_vram = None
        self.total_ram = round(psutil.virtual_memory().total / 1024**3, 2)

    # ----------------------------------------------------
    # GPU
    # ----------------------------------------------------

    def _get_gpu_stats(self):
        """
        Returns GPU statistics using nvidia-smi.
        """

        try:

            cmd = [
                "nvidia-smi",
                "--query-gpu=name,"
                "utilization.gpu,"
                "memory.used,"
                "memory.total,"
                "temperature.gpu,"
                "power.draw",
                "--format=csv,noheader,nounits"
            ]

            output = subprocess.check_output(cmd).decode().strip()

            # print("\n===== NVIDIA OUTPUT =====")
            # print(output)
            # print("=========================\n")

            values = [x.strip() for x in output.split(",")]

            # print(values)

            gpu_name, gpu_util, mem_used, mem_total, temp, power = values

            power = power.strip()

            # if "N/A" in powe:
            #     gpu_power = None
            
            # else:
            #     gpu_power = float(power)
            try:
                gpu_power = float(power)
            
            except ValueError:
                gpu_power = None

            return {
            "gpu_name": gpu_name,
            "gpu_util": float(gpu_util),
            "gpu_mem": float(mem_used),
            "gpu_total": float(mem_total),
            "gpu_temp": float(temp),
            "gpu_power": gpu_power,
             }

        except Exception as e:
             print("GPU ERROR:", e)
             return {
            "gpu_name": "Unknown",
            "gpu_util": 0.0,
            "gpu_mem": 0.0,
            "gpu_total": 0.0,
            "gpu_temp": 0.0,
            "gpu_power": None,
             }

            # print(output)

            # gpu_name, gpu_util, mem_used, mem_total, temp, power = \
            #     [x.strip() for x in output.split(",")]

            # if power == "N/A":
            #     power = None
            # else:
            #     power = float(power)

            # return {

            #     "gpu_name": gpu_name,

            #     "gpu_util": float(gpu_util),

            #     "gpu_mem": float(mem_used),

            #     "gpu_total": float(mem_total),

            #     "gpu_temp": float(temp),

            #     "gpu_power": power
            # }

        # except Exception as e:

        #     print(e)

            # return {

            #     "gpu_name": None,

            #     "gpu_util": 0,

            #     "gpu_mem": 0,

            #     "gpu_total": 0,

            #     "gpu_temp": 0,

            #     "gpu_power": None
            # }

    # ----------------------------------------------------
    # CPU / RAM
    # ----------------------------------------------------

    def _get_system_stats(self):

        memory = psutil.virtual_memory()

        return {

            "cpu": psutil.cpu_percent(interval=None),

            "ram_used": round(memory.used / 1024**3, 2),

            "ram_total": round(memory.total / 1024**3, 2)
        }

    # ----------------------------------------------------
    # One Sample
    # ----------------------------------------------------

    def _collect(self):

        gpu = self._get_gpu_stats()

        cpu = self._get_system_stats()

        if self.gpu_name is None:
            self.gpu_name = gpu["gpu_name"]

        if self.total_vram is None:
            self.total_vram = gpu["gpu_total"]

        sample = {

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            **gpu,

            **cpu
        }

        self.samples.append(sample)

    # ----------------------------------------------------
    # Thread Loop
    # ----------------------------------------------------

    def _monitor(self):

        while self.running:

            self._collect()

            time.sleep(self.interval)

    # ----------------------------------------------------
    # Public API
    # ----------------------------------------------------

    def start(self):

        self.samples = []

        self.running = True

        self.thread = threading.Thread(target=self._monitor)

        self.thread.daemon = True

        self.thread.start()

    def stop(self):

        self.running = False

        if self.thread:
            self.thread.join()

    # ----------------------------------------------------
    # Summary
    # ----------------------------------------------------

    def summary(self):

        if len(self.samples) == 0:
            return {}

        def values(key):

            return [
                x[key]
                for x in self.samples
                if x[key] is not None
            ]

        gpu_util = values("gpu_util")
        gpu_mem = values("gpu_mem")
        gpu_temp = values("gpu_temp")
        cpu = values("cpu")
        ram = values("ram_used")
        gpu_power = values("gpu_power")

        return {

            "GPU Name": self.gpu_name,

            "Total VRAM (MB)": self.total_vram,

            "Total RAM (GB)": self.total_ram,

            "Avg GPU Util (%)": round(mean(gpu_util), 2),
            "Peak GPU Util (%)": max(gpu_util),

            "Avg VRAM Used (MB)": round(mean(gpu_mem), 2),
            "Peak VRAM Used (MB)": max(gpu_mem),

            "Max GPU Temp (C)": max(gpu_temp),

            "Avg CPU (%)": round(mean(cpu), 2),
            "Peak CPU (%)": max(cpu),

            "Avg RAM Used (GB)": round(mean(ram), 2),
            "Peak RAM Used (GB)": max(ram),

            "Max GPU Power (W)": (
                max(gpu_power)
                if len(gpu_power) > 0
                else None
            )
        }