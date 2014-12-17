#!/bin/bash

TICKETID="$1"
TICKETCOMMENT="$2"

IP="192.168.1.153"
UPDATETICKETURL="https://raw.githubusercontent.com/sp-chenyang/xxutils/master/updateticket.py?$RANDOM"

# 192.168.1.153
UPDATETICKETPY="/tmp/updateticket.py"

# debug param
echo "[replyticket.sh] \$1 = [$1]"
echo "[replyticket.sh] \$2 = [$2]"

#
# prepare working env
#

# 192.168.2.21
mkdir -p "/tmp/xxutils"
XXUTILS="/tmp/xxutils/xxutils.sh"

# load useful functions
wget -q https://raw.githubusercontent.com/sp-chenyang/xxutils/master/xxutils.sh?$RANDOM -O $XXUTILS \
    && chmod a+x $XXUTILS \
    && . $XXUTILS
if [ $? != 0 ]
then
    exit 1
fi

# create working dir (random dir) for me, on 192.168.2.21
JDIR=$( gettmpdir "xuanran001_webapi_unittest" )
cd "$JDIR"
CMDFILE="$JDIR/updateticket_rcmd.sh"

# prepare remote shell script
echo "" > $CMDFILE

#
# begin to update a ticket
#


echo "curl $UPDATETICKETURL -o $UPDATETICKETPY" >> $CMDFILE
echo "comment=\"$TICKETCOMMENT\"" >> $CMDFILE
cmd="$cmd sudo python $UPDATETICKETPY"
cmd="$cmd --id $TICKETID"
cmd="$cmd --comment \"\$comment\""
cmd="$cmd --author \"chenyang\""
echo $cmd >> $CMDFILE

# just for debug
cat $CMDFILE

rcmdfile "$IP" "$CMDFILE"
