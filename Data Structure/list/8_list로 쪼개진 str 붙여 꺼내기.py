# python���� string�� list�� ���� ��� �� �� �� �ڰ� �ٸ� item�� �ǰ� �Ѵ�.
# �׷��� ���ε��� ������ ���ڵ��� ��� ���� ���·� �����, list������ ������ ���� �� ����Ѵ�.


# str
example_str = 'melancholy'

# list�� �����
example_li = list(example_str)
print(example_li)

# list���� ������
back_str = ''.join(example_li)
print(back_str)

# ���� str
example_sentence = 'Am I blue?'

# list�� �����
example_li2 = list(example_sentence)
print(example_li2)

# list���� ������(���� ������� ����)
back_sentence = ''.join(example_li2)
print(back_sentence)

# list���� ������(���� ���)
back_sentence = ' '.join(example_li2)
print(back_sentence)
