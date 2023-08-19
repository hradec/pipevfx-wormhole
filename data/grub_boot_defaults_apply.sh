#!/bin/bash

CD=$(dirname $(readlink -f $0))
grub=$(dirname $( readlink -f $CD/grub_boot_defaults))

echo  $grub
cmd="ssh localhost \"cd $grub && pwd && make\""
echo $cmd
eval "$cmd"
