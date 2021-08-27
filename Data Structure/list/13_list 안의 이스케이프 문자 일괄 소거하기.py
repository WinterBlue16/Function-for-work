# 크롤링 시, 리스트 안의 값들이 이스케이프 문자(ex.\n, 참고 : http://blog.naver.com/PostView.nhn?blogId=vslinux&logNo=220592885994)와 함께 들어가 있을 때가 있다.
# 이스케이프 문자만 제거하고 싶을 때 활용할 수 있다.

# 실험용 데이터(실제 크롤링으로 가져온 데이터)
sample_df = ['\n[금자희재] 일상의새벽\n', '\n[금자희재]회자정리(會者定離)-3\n', '\n[금자희재] If The World Was Ending\n', '\n무제 (11)\n', '\n[금자희재] Blood//Water\n',
             '\n[연홍이창/금자희재] 인因(5)\n', '\n2020-03 백업 05\n', '\n[금자희재] Our Shining Days\n', '\n[금자희재/희재금자] 난파선 下\n', '\n[금자희재/희재금자] 난파선 上\n', '\n놀이터\n']

# 이스케이프 문자 제거
# 방법 1
sample_df = [text.strip() for text in sample_df]

# 방법 2
sample_df = list(map(lambda x: x.strip(), sample_df))
