# 1
# 처음부터 gqu 메모리가 적은 비율만 할당되도록 설정
# 프로세스의 메모리 수요에 따라 증가
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sessions = tf. Session(config=config)


# 2
# gpu에 어느 비율만큼의 메모리를 할당할지 미리 지정
# 프로세스가 어느 정도의 메모리를 사용할지 알고 있다면, 미리 그만큼 지정해두어 메모리 절약 가능
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.4
session = tf.Session(config=config)


# 출처 및 참고 : https://datamasters.co.kr/33
