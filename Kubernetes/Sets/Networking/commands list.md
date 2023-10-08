## Show ip addressed of the devices and mac address: **ip addr show** 

## Show linked devies: **ip link show**

## Show only listening ports: **ss -nlpt** 

## Show only bridge type devices :ip addr type bridge

## To get the internal ip of the nodes: kubectl get nodes -o wide

## Add a route table: ip addr add route 10.244.1.0/24 via 192.168.1.1/24

## Get the container runtime: ps aux|grep kubelet| grep container-runtime

## All the CNI plugins are stored here : /opt/cni/bin

## CNI plugin configured to use: /etc/cni/net.d

## Service in K8s are cluster wide.

## Find node ranege: Inspect the node's internal IP Kubectl get nodes -o wide

## Pods IP:- Find the networking system first then inspect the logs of the pod for that service

## Type of proxy: inspect the logs of the pod kube-proxy

## 