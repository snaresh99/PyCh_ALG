import numpy as np
from PyDAQmx import Task, DAQmx_Val_Cfg_Default, DAQmx_Val_Volts, DAQmx_Val_Rising, DAQmx_Val_ContSamps, DAQmx_Val_GroupByChannel
from PyDAQmx.DAQmxTypes import int32, float64, byref
import matplotlib.pyplot as plt

# Define a callback function for data acquisition
class AnalogInput(Task):
    def __init__(self, num_samples=4000):
        Task.__init__(self)
        self.num_samples = num_samples
        self.CreateAIVoltageChan("Dev1/ai0", "", DAQmx_Val_Cfg_Default, -10.0, 10.0, DAQmx_Val_Volts, None)
        self.CfgSampClkTiming("", 1000.0, DAQmx_Val_Rising, DAQmx_Val_ContSamps, 1000)

    def read_data(self):
        data = np.zeros((self.num_samples,), dtype=np.float64)
        read = int32()
        self.ReadAnalogF64(self.num_samples, 20.0, DAQmx_Val_GroupByChannel, data, self.num_samples, byref(read), None)
        print("byref(read): is the address of read", byref(read))
        print("DAQmx Group by channel", DAQmx_Val_GroupByChannel)
        print("DAQmx Val rising:", DAQmx_Val_Rising)
        print("DAQmx Continuous Samples", DAQmx_Val_ContSamps)
        print("DAQmx Val Cfg Default", DAQmx_Val_Cfg_Default)
        print("DAQmx Val Volts", DAQmx_Val_Volts)

        return data

if __name__ == "__main__":
    # Usage
    ai_task = AnalogInput(num_samples = 10000)
    ai_task.StartTask()
    data = ai_task.read_data()
    ai_task.StopTask()
    ai_task.ClearTask()
    print(data)
    plt.plot(data)
    plt.show()
