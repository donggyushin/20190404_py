# ham의 배열은 [0,1]이 됨. eggs=[2,3] 때문에 ham 또한 [2,3] 으로 바뀔 것 같지만	
# spam 내부에서만 변화하고 실제론 변화하지 않음
# ham 의 주소값이 전달되는게 아니라 value 값만 전달되기 때문임
def spam(eggs):
    eggs.append(1)

    eggs = [2,3]

ham = [0]
spam(ham)
print(ham)
