########################################################################
# Copyright 2017 FireEye Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
########################################################################

import time
import sys
import etw

# append the path of pywintrace-master
sys.path.append('''C:\\Users\\tyh\\desktop\\pywintrace-master''')


# python -u "C:\Users\tyh_2\desktop\pywintrace-master\examples\simple2.py"

def some_func():
    # define capture provider info

    providers0 = [etw.ProviderInfo('PowerShell', etw.GUID("{A0C1853B-5C40-4B15-8766-3CF1C58F985A}"))]
    providers1 = [etw.ProviderInfo('Kernel-Registry', etw.GUID("{70EB4F03-C1DE-4F73-A051-33D13D5413BD}"))]
    providers2 = [etw.ProviderInfo('Kernel-Network', etw.GUID("{7DD42A49-5329-4832-8DFD-43D979153A88}"))]
    providers3 = [etw.ProviderInfo('Kernel-File', etw.GUID("{EDD08927-9CC4-4E65-B970-C2560FB5C289}"))]
    providers4 = [etw.ProviderInfo('Kernel-Audit-API-Calls', etw.GUID("{E02A841C-75A3-4FA7-AFC8-AE09CF9B7F23}"))]
    providers5 = [etw.ProviderInfo('Kernel-Disk', etw.GUID("{C7BDE69A-E1E0-4177-B6EF-283AD1525271}"))]
    providers6 = [etw.ProviderInfo('HttpEvent', etw.GUID("{7B6BC78C-898B-4170-BBF8-1A469EA43FC5}"))]
    providers7 = [etw.ProviderInfo('HttpLog', etw.GUID("{C42A2738-2333-40A5-A32F-6ACC36449DCC}"))]
    providers8 = [etw.ProviderInfo('HttpService', etw.GUID("{DD5EF90A-6398-47A4-AD34-4DCECDEF795F}"))]

    # change providers0 to providers1,2,..8 to get other logs
    job0 = etw.ETW(providers=providers3, event_callback=lambda x: print(x))
    job0.start()
    print('start')
    time.sleep(100)
    print('end')
    job0.stop()


if __name__ == '__main__':
    some_func()

