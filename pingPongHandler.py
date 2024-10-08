import types
import time
import random
from DIRAC import S_OK, S_ERROR, gLogger
from DIRAC.Core.Utilities import DEncode
from DIRAC.Core.Base.ExecutorMindHandler import ExecutorMindHandler

random.seed()

class PingPongHandler( ExecutorMindHandler ):
	MSG_DEFINITIONS = { 'StartReaction' : { 'numBounces' : ( types.IntType, types.LongType ) } }
	auth_msg_StartReaction = [ 'all' ]
	def msg_StartReaction( self, msgObj ):
		bouncesLeft = msgObj.numBounces
		taskid = time.time() + random.random()
		taskData = { 'bouncesLeft' : bouncesLeft }
		return self.executeTask( time.time() + random.random(), taskData )
		auth_startPingOfDeath = [ 'all' ]
		types_startPingOfDeath = [ types.IntType ]
	def export_startPingOfDeath( self, numBounces ):
		taskData = { 'bouncesLeft' : numBounces }
		gLogger.info( "START TASK = %s" % taskData )
		return self.executeTask( int( time.time() + random.random() ), taskData )

@classmethod
def exec_executorConnected( cls, trid, eTypes ):
	gLogger.info( "EXECUTOR CONNECTED OF TYPE %s" % eTypes )
	return S_OK()

@classmethod
def exec_executorDisconnected( cls, trid ):
	return S_OK()

@classmethod
def exec_dispatch( cls, taskid, taskData, pathExecuted ):
	gLogger.info( "IN DISPATCH %s" % taskData )
	if taskData[ 'bouncesLeft' ] > 0:
		gLogger.info( "SEND TO PLACE" )
		return S_OK( "Test/PingPongExecutor" )
	return S_OK()

@classmethod
def exec_prepareToSend( cls, taskId, taskData, trid ):
	return S_OK()

@classmethod
def exec_serializeTask( cls, taskData ):
	gLogger.info( "SERIALIZE %s" % taskData )
	return S_OK( DEncode.encode( taskData ) )

@classmethod
def exec_deserializeTask( cls, taskStub ):
	gLogger.info( "DESERIALIZE %s" % taskStub )
	return S_OK( DEncode.decode( taskStub )[0] )

@classmethod
def exec_taskProcessed( cls, taskid, taskData, eType ):
	gLogger.info( "PROCESSED %s" % taskData )
	taskData[ 'bouncesLeft' ] -= 1
	return cls.executeTask( taskid, taskData )

@classmethod
def exec_taskError( cls, taskid, taskData, errorMsg ):
	print "OOOOOO THERE WAS AN ERROR!!", errorMsg
	return S_OK()

@classmethod
def exec_taskFreeze( cls, taskid, taskData, eType )
	print "OOOOOO THERE WAS A TASK FROZEN"
	return S_OK()

