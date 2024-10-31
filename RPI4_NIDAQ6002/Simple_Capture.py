import numpy as np
from PyDAQmx import Task
import PyDAQmx
import matplotlib.pyplot as plt

# Define a callback function for data acquisition
class AnalogInput(Task):
    def __init__(self):
        Task.__init__(self)
        self.CreateAIVoltageChan("Dev1/ai0", "", PyDAQmx.DAQmx_Val_Cfg_Default, -10.0, 10.0, PyDAQmx.DAQmx_Val_Volts, None)
        self.CfgSampClkTiming("", 1000.0, PyDAQmx.DAQmx_Val_Rising, PyDAQmx.DAQmx_Val_ContSamps, 1000)

    def read_data(self):
        data = np.zeros((4000,), dtype=np.float64)
        read = PyDAQmx.int32()
        self.ReadAnalogF64(4000, 10.0, PyDAQmx.DAQmx_Val_GroupByChannel, data, 4000, PyDAQmx.byref(read), None)
        return data

# Usage
ai_task = AnalogInput()
ai_task.StartTask()
data = ai_task.read_data()
ai_task.StopTask()
ai_task.ClearTask()
print(data)
plt.plot(data)
plt.show()
