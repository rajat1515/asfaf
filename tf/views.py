from django.shortcuts import render
from .main import Calculate
def home(request):		
	return render(request,'home.htm')

def submit(request):
	if request.method == "POST":
		A=request.POST.get('A')
		B=request.POST.get('B')
		C=request.POST.get('C')
		D=request.POST.get('D')
		E=request.POST.get('E')
		F=request.POST.get('F')
		G=request.POST.get('G')
		H=request.POST.get('H')
		I=request.POST.get('I')
		
		q={1:int(A),2:int(B),3:int(C),4:int(D),5:int(E),6:int(F),7:int(G),8:int(H),9:int(I)}

		c=Calculate()
		c.checkset(q)
		cc=c.tcost(0,q)

		#print(cc)

		
	return render(request,'home.htm',{'value':cc})