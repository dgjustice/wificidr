"""
>>> import pandas as pd
>>> df = pd.read_csv("pcap.csv")
>>> df
           No.         Time          Source    Destination Protocol  Length                                               Info
0            1     0.000000    52.9.241.102  192.168.1.248  TLSv1.2     105                                   Application Data
1            2     0.002925   50.18.200.106  192.168.1.248  TLSv1.2     105                                   Application Data
2            3     0.153498    34.194.201.2  192.168.1.248      TCP      66  443  >  41732 [ACK] Seq=1 Ack=1 Win=9 Len=0 TS...
3            4     0.156735    34.194.201.2  192.168.1.248      TCP      66  443  >  41734 [ACK] Seq=1 Ack=1 Win=8 Len=0 TS...
4            5     1.134049    34.194.201.2  192.168.1.248      TCP      66  443  >  41732 [ACK] Seq=1 Ack=57 Win=9 Len=0 T...
...        ...          ...             ...            ...      ...     ...                                                ...
136087  136088  9494.215607   192.168.1.229  192.168.1.248      TCP     183  8009  >  49494 [PSH, ACK] Seq=222930 Ack=22294...
136088  136089  9494.276939    34.194.201.2  192.168.1.248  TLSv1.2     153                                   Application Data
136089  136090  9494.447930    192.80.8.129  192.168.1.248      UDP     263                             1195  >  44889 Len=221
136090  136091  9494.454119  54.241.191.232  192.168.1.248      TCP      60  [TCP Dup ACK 135606#7] 443  >  40664 [ACK] Seq...
136091  136092  9494.657938  149.56.134.238  192.168.1.248  TLSv1.3     174                                   Application Data

[136092 rows x 7 columns]
>>>
"""

"""
The following code demonstrates the equations and calculations found at
https://sflow.org/packetSamplingBasics/index.htm
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pcap.csv")

# Randomly-picked host
host = "34.194.201.2"

# population_prop = len(df[df.Source == host]) / df["No."].max()

"""
Equation 1
"""
# 340 ~ 0.25%
n = 340
N = df["No."].max()
samples = df.sample(n=n, random_state=1)
c = len(samples[samples["Source"] == host])
N_c = c / n * N

"""
Equation 2
"""
sig_sq = (N**2) * (c* (1 - c / n))/(n**2 - n)

top_talkers = df.groupby(["Source"]).size().to_frame("size").reset_index().sort_values(["size"], ascending=False).head(10)

plt.hist(top_talkers["Source"], 10, normed=1)
plt.yscale('log')
plt.show()
