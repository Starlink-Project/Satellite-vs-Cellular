# Satellite-vs-Cellular

In this repository, we release the dataset and tools in [CoNEXT '23](https://conferences2.sigcomm.org/co-next/2023/) paper, *LEO Satellite vs. Cellular Networks: Exploring the Potential for Synergistic Integration*.

## Introduction

In this work, we present a measurement study of the Starlink LEO satellite network in comparison with cellular networks, aiming to uncover the potential for synergistic integration. Through a large-scale data collection campaign and in-depth analysis, we (1) identify the performance characteristics of two Starlink configurations, (2) evaluate the coverage of the current Starlink deployment compared to major cellular carriers, and (3) investigate the potential benefits of enabling multipath using both LEO satellite and cellular networks.

To help you easily obtain the figures presented in this paper, we have provided complete scripts and processed data, which come with detailed instructions. The folders and files are organized in the order of the figures as they appear in the paper. Most of the figures can be generated by simply running a single command.

## Dataset

#### Data Collection

We use the [Mobility](https://www.starlink.com/mobility) (MOB) and [Roam](https://www.starlink.com/roam) (RM) plans of Starlink and three cellular carriers, together with three cellular carriers in ths US. We use five smartphones, each connected to one of these services.

We perform extensive drive tests across major cities and interstate freeways in the US. It encompasses diverse geographical regions, including densely populated urban areas with tall buildings and open rural areas with minimal obstructions.

#### Paper Structure to Folder Structure

| Content in Paper | Folder in Repo |  Description |
|:---:|:---:|:---:|
| Figure 1 | [Downlink-Thrpt](1-Downlink-Thrpt) | Examples of download throughput of different networks over time. |
| Figure 3 | [Thrpt-Comp](3-Thrpt-Comp) | Throughput performance comparison from different aspects. |
| Figure 4 | [UDP-Ping-Latency](4-UDP-Ping-Latency) | UDP Ping latency results of Starlink and cellular networks |
| Figure 5 | [TCP-Packet-Loss](5-TCP-Packet-Loss) | TCP packet loss rate results of Starlink and cellular networks |
| Figure 6 | [Driving-Speed](6-Driving-Speed) | Relationship of throughput and moving speed for Starlink and cellular networks. |
| Figure 7 | [TCP-Parallel](7-TCP-Parallel) | Impact of TCP parallelism on TCP throughput for Starlink and cellular networks. |
| Figure 8 | [Area-Type](8-Area-Type) | Impact of area types on network throughput of Starlink and cellular networks |
| Figure 9 | [Perf-Coverage](9-Perf-Coverage) | Network performance coverage of various networks. |
| Figure 10 | [MPTCP-Stats](10-MPTCP-Stats) | Performance comparison between single-path TCP and MPTCP on file download. |
| Figure 11 | [MPTCP-Thrpt](11-MPTCP-Thrpt) | Examples of throughput progression over time for single-path TCP and MPTCP. |

As always, if there are any questions, feel free to reach out to us (hubin@usc.edu, xumiao@umich.edu)!
