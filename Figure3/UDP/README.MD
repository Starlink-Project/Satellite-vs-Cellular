# UDP Throughput Measurement

This folder contains the dataset for UDP Downlink and uplink throughput measurement via Starlink and cellular networks conducted using **5GTracker**.

## Folder Structure   

| Filename                    | Description                                                                                                |
|-----------------------------|------------------------------------------------------------------------------------------------------------|
| `Downlink/[Network Provider]_all_area.csv` | UDP Downlink Throughput logs for both Starlink and cellular networks.|
| `Uplink/[RV-In-motion_all_area.csv` | UDP Uplink Throughput logs for Starlink Mobility plan.|

## Dataset Description

The dataset files `AT_T_all_area1.csv`, `RV-In-motion_all_area1.csv`, `T-mobile_all_area1.csv`, and `Verizon_all_area1.csv` contain several fields. We provide descriptions for each field below.

| Field name           | Description of the field                                           |
|----------------------|--------------------------------------------------------------------|
| `time`               | Timestamp of the test                           |
| `throughput`         | Downlink throughput in Megabits per second (Mbps)                  |
| `speed`        | Driving speed while experiments in miles per hour (Mph)                   |
| `latitude`         | Latitude of the location while experiments                             |
| `longtitu`    |Longitude of the location while experiments|
| `area_type`    |Area type of the location while experiments|
