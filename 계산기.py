##합수
def add_func(n1,n2):
    return n1+n2
def sub_func(n1,n2):
    return n1-n2
def mul_func(n1,n2):
    return n1*n2
def div_func(n1,n2):
    return n1/n2
def res_func(n1,n2):
    return n1%n2
def pow_func(n1,n2):
    return n1**n2
##변수
num1,num2 = 0,0
##메인

#두 숫자의 더하기/빼기 등등을 계산하기
num1 = int(input("숫자1:"))
num2 = int(input("숫자2:"))
result = add_func(num1,num2)
print(num1,'+',num2, "=", result)

result = sub_func(num1,num2)
print(num1,'-',num2, "=", result)

result = mul_func(num1,num2)
print(num1,'*',num2, "=", result)

result = div_func(num1,num2)
print(num1,'/',num2, "=", result)

result = res_func(num1,num2)
print(num1,'%',num2, "=", result)

result = pow_func(num1,num2)
print(num1,'**',num2, "=", result)

# 더하기  +
# 빼기   -
# 곱하기     *
# 나누기     /
# 몫    //
# 나머지     %
# 제곱  **

