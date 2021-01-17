Client                                                         Server
=============================================================================
                                                               LISTEN
            > flags=SYN seq=<random1> length=0
SYN-SENT
            < flags=SYN seq=<random2> ack=random1+1 length=0
                                                               SYN-RECEIVED
            > ack=1 length=0
ESTABLISHED                                                    ESTABLISHED

            > flags=P seq=1:<int1> ack=1 length>0
            < ack=int1 length=0
            .............

-----------------------------------------------------------------------------
            > flags=F seq=int1 ack=<int2> length=0
FIN_WAIT_1
            < ack=int1+1 length=0
                                                               CLOSE_WAIT
FIN_WAIT_2
            < flags=F seq=int2 ack=int1+1 length=0
(TIME_WAIT)
                                                               LAST_ACK
            > ack=int2+1 length=0
CLOSED                                                         CLOSED
