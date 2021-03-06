import random


import getopt
import sys
import commands

#+++++++++++++++++++------________________________
#** S E T T I N G S
#-------------------------------------------------
CLIENT_PUBLIC = '1C9EE378'
#-------------------------------------------------


#-------------------------------------------------
# ** T E S T phrase
TEST_SEC_MSG = "7;W^0B9JTTR6I7<SW==ZQDPB>FR>QE3E>@_DGVXBV94SA@UIWH^N5MM@;7^D93WF_DO0:385YUPPQXHBAKAY=3D5LLM4EGY??IONQ0IV0KBDUX[[6WN2EUBU7W6486>OGNB[:PZ94;O@KY[T3WA__621@F@3OZS8JRK7IITJ;EK_@CY7DES9U<PA4_S_=PK@KRYL[VX4IP?JUYGC?[M_VZ<C^A^LB?4R5T89^@Q]_EVV]^XESPAS0U>[=4^5SK9?]2NC2?ZPOE4X@:ELWQ6RKLA?SP0F>6:^G8ZWA0;ISYGH5SNID_<_FTM05IW4>WN78A;X^G1>TFFZ26EFV^VK:S3LO3^ZBQB;4^4HCR2R=[D[M^2?2KJ=MJI[S6=^SC0;3]DMT^>__[U>C?4J:<LKCS[P08QV_C;G9U27ZQ?:;;;HICB[M4TD>8@@[G;_;B3BII575H9MCAM@S]8IWGF_W=G986GHQ8TE3PPPZSE0<?^W9V<C0EMO<3_]OE^1[:H^GJ4EVJSFY2H6@T<VC?@MT77CU1GS3VV_L?SB^_^QY^O6VTU5BLCBGWE^I2QRA1L_OU9Z]@OYCE@EI7:ZEGR<MM;H39HUR77PSF3<;F0M1;=B21]6=]122:XHTR>OR2]>[CPZ0Q93YV57O;5TN_45BFI874FJY5NPWU:J^<MFI1UX0@TFGF==BPK0:0YZ1M@Z5?2L72UH9B1_;I7C4=>:MEXAN5OQ<>HBA=Y4X8OATT<E@IA9_]XW6R98K>V8HUU3U>VGAH46G?D06E[;I_G67]J;5?D3ZHH3?V6Q=WM6[1];YXCYN=8_QHN027>RL6U];_@PKSG0]Z5HFNKD:9L?BWMJ8^VT7?PT76L1<[20^1VOFUCH0Q;^PVA65W>U[SZY;0_5RS:SRN9SQPDGM?E9UIMLC4D>_R@63>;M0VJOWOZO87T_33CL=WUPTU=N4;:UTI4CG_^=H61CIVFQ_G575DBL0D=HAE5E86J0>_@GE8B6N7SD61BX4:Z>EO1D=[NB36QA:?70S9_DHB8WL_[JSRTWTAQ_:5>5PQ8F2[;[J:RI;BXVQGE4MHHG<^_BK2KLLRVA>MI8IK<EJYDT2==X0N<_>LCQYM?TRNDYD_4=RU41KGXK=O6J?NAQL[Y^4W@Z0=RMYR4>6LNSO[Y3:=USKWY3I[8X2DU8F0FK?;F9HM6^UFPQMV9[H@L>FU18]0U1@6Q05YFT8SW4_1YKY2R98DTJMBBV6>F>I[H0<K>_9A3V4GIVZ_G0IUO;=@]3PIL_Z_P]W8^VGDX7S4CDYKCR:L[>2>2EYDZ4A=R[ZNF>=@[ZJ7=6[SS>H7UJ7QASBZ7IE9Z6Z4NKXX9R13_HFSV092C7P<5ILHJHEGK[D;GZX9Q3@V_S87@B?_^D3QC6SC=VQZK1ON8S6MUUTTGO^CY=4>?>GSXW8AP6EQ@CR?SNTYUKRQ0OH?ELFKO]F0RZ^R<3H85@P3L7TTQU4S8[F?CD:@8X1R^W_>55QZGXS31LC;41?CZOR0QQWNDANZYJA?5?5K[;G[ZBT4VT9ENF@V05II@:77V:PY5PA@FG@4:WA5WS5C9USHE1F_KG?<AMTC1NDSJ;UXC24Y9?>R]@CTR?K>W:];G@6[VRVQ7B^QPD>7_MPDB?=4<3?VS8F=>@GKCV4H6@UTYQG>J@QS_G8>EE>FBGWKJJ@8U0]U=KO]DT][2KG@41Q5=EQXK<]88RD8=4=?[YHW4L1"	


def Gen_Sec_Message(DEBUG, DEBUG_NO_CARD):
    if DEBUG_NO_CARD:
	sec_message = TEST_SEC_MSG
    else:
	sec_message = Random_Message(random.randint(1500,2048))
    if DEBUG:
	print sec_message	  
    return sec_message  


def Random_Message(number_of_chars):
    message = '';
    print 'n = ', number_of_chars
    for i in range(number_of_chars):
      sec_char = chr(random.randint(48,95))
      if sec_char not in "'\\":
	message = message + sec_char
    print 'l = ', len(message)
    return message;  

def Encrypt_Sec_Message(sec_message, DEBUG, DEBUG_NO_CARD):
    if not DEBUG_NO_CARD:
	gpg_en = commands.getoutput('echo \'%s\' | gpg --encrypt --armor -r \'%s\'' %(sec_message, CLIENT_PUBLIC))
	if DEBUG:
	    print "func ENC_SEC_MSG, DECRYPTED MSG: %s" % gpg_en
	return gpg_en
    return TEST_SEC_MSG
    
    
def Confirm_Message(encrypted_msg, sec_message, DEBUG, DEBUG_NO_CARD):
    if encrypted_msg == 0:
	print "ERROR, communication failed"
	return 111
    print "Please confirm your IDENTITY!"
    if DEBUG_NO_CARD:
	decrypted_sec_msg = TEST_SEC_MSG
    else:
	decrypted_sec_msg = commands.getoutput('echo \'%s\' | gpg -d' % encrypted_msg)
   
    if DEBUG:
	print "DECRYPTED MSG:\n %s \n LEN: %d " % (decrypted_sec_msg, len(decrypted_sec_msg))
	print "SEC_MSG______:\n %s \n LEN: %d " % (sec_message, len(sec_message))
	
    decrypted_sec_msg = decrypted_sec_msg[-len(sec_message):]
    if DEBUG:
      print "DEC MSG CHANGED"
      print decrypted_sec_msg
      
      f = open('a.log', 'w');
      f.write(str(len(decrypted_sec_msg))+'\n');
      for i in xrange(0, len(decrypted_sec_msg)):
	  f.write(str(ord(decrypted_sec_msg[i]))+'\n');
      f.close();

      f = open('b.log', 'w');
      f.write(str(len(sec_message))+'\n');
      for i in xrange(0, len(sec_message)):
	  f.write(str(ord(sec_message[i]))+'\n');
      f.close();

    if decrypted_sec_msg == sec_message:
	print "OK, process was sucessful"
	return 1
    else:
	print "!!! INTRUDER ALERT !!!"
	return 0
