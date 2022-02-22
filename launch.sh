#!/bin/bash
docker run -p 8088:8088 -p 9870:9870 -p 8020:8020 -p 8031:8031 -t -d vovanoti/headnode
docker run -p 8042:8042 -t -d vovanoti/worker
