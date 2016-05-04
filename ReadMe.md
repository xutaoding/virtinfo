Virtual memory size
===================

This script run command of linux to Judge process virtual memory to exceed expected size
whether or not


Sample:
-------
cmd= 'ps aux|grep java'

vsi = VirtualSizeInfo(cmd)

print vsi.pid

print vsi.virtual_size

print vsi.is_exceed
