# AzureNSGFlowLogReader
Takes a base flow log from azure flow logs and creates baseic pretty print table for it


Creates tables as follows

# DefaultRule_AllowInternetOutBound
```python
+------------+------------+----------------+---------+----------+------+--------+--------+----------+----------+---------+-----------+---------+
|    Time    |  SourceIP  |     DestIP     | SrcPort | DestPort | Prot | Fl_dir | Fl_act | Fl_state | Pckt_Snt | Byt_snt | Pckt_rcvd | Byt_rcv |
+------------+------------+----------------+---------+----------+------+--------+--------+----------+----------+---------+-----------+---------+
| 1680985786 | 100.254.1.6| 51.132.193.10  |  63636  |   443    |  T   |   O    |   A    |    B     |          |         |           |         |
| 1680985796 | 11.254.1.6 | 52.239.161.4   |  63581  |   443    |  T   |   O    |   A    |    E     |    16    |   9708  |     13    |   7739  |
| 1680985796 | 19.254.1.6 |  23.99.80.1    |  63582  |   443    |  T   |   O    |   A    |    E     |    16    |   7181  |     12    |   5786  |
| 1680985805 | 18.254.1.6 | 20.190.51.13   |  63642  |   443    |  T   |   O    |   A    |    B     |          |         |           |         |
+------------+------------+----------------+---------+----------+------+--------+--------+----------+----------+---------+-----------+---------+


```python
# DefaultRule_AllowVnetOutBound
+------------+------------+------------+---------+----------+------+--------+--------+----------+----------+---------+-----------+---------+
|    Time    |  SourceIP  |   DestIP   | SrcPort | DestPort | Prot | Fl_dir | Fl_act | Fl_state | Pckt_Snt | Byt_snt | Pckt_rcvd | Byt_rcv |
+------------+------------+------------+---------+----------+------+--------+--------+----------+----------+---------+-----------+---------+
| 1680985786 | 14.243.1.6 | 10.264.1.7 |  63634  |   135    |  T   |   O    |   A    |    B     |          |         |           |         |
| 1680985786 | 12.253.1.6 | 10.274.1.7 |  63635  |  49671   |  T   |   O    |   A    |    B     |          |         |           |         |
| 1680985802 | 9.252.1.6  | 10.284.1.7 |  63634  |   135    |  T   |   O    |   A    |    E     |    7     |   718   |     5     |   658   |
| 1680985802 | 10.231.1.6 | 10.294.1.7 |  63635  |  49671   |  T   |   O    |   A    |    E     |    7     |   862   |     5     |   754   |
+------------+------------+------------+---------+----------+------+--------+--------+----------+----------+---------+-----------+---------+

