#!/usr/bin/env python
from mpi4py import MPI
import sys
import time
from DIRAC import S_OK, S_ERROR
from DIRAC.Core.Base import Script
from DIRAC.Core.DISET.MessageClient import MessageClient

Script.parseCommandLine()

def sendPingMsg( msgClient, pingid = 0 ):
	result = msgClient.createMessage( "Ping" )
	if not result[ 'OK' ]:
	return result
	msgObj = result[ 'Value' ]
	msgObj.id = pingid
	return msgClient.sendMessage( msgObj )

def pong( msgObj ):
	pongid = msgObj.id
	print "RECEIVED PONG %d" % pongid
	return sendPingMsg( msgObj.msgClient, pongid + 1 )
	def disconnectedCB( msgClient ):
	retryCount = 0
	while retryCount:
	result = msgClient.connect()
	if result[ 'OK' ]:
	return result
	time.sleep( 1 )
	retryCount -= 1
	return S_ERROR( "Could not reconnect... :P" )

if __name__ == "__main__":
	msgClient = MessageClient( "Framework/PingPong" )
	msgClient.subscribeToMessage( 'Pong', pongCB )
	msgClient.subscribeToDisconnect( disconnectedCB )
	result = msgClient.connect()
	if not result[ 'OK' ]:
	print "CANNOT CONNECT: %s" % result[ 'Message' ]
	sys.exit(1)
	result = sendPingMsg( msgClient )
	if not result[ 'OK' ]:
	print "CANNOT SEND PING: %s" % result[ 'Message' ]
	sys.exit(1)
	#Wait 10 secs of pingpongs :P
	time.sleep( 10 )
	size = MPI.COMM_WORLD.Get_size()
	rank = MPI.COMM_WORLD.Get_rank()
	name = MPI.Get_processor_name()
	sys.stdout.write("Hello, World! I am process %d of %d on %s.\n" % (rank, size, name))