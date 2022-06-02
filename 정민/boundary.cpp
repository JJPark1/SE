#include <string>
#include "boundary.h"
ifstream fin;

JoinUI::JoinUI(Join* j) :join(j) {}

void JoinUI::join_function()
{ // 바운더리

	string name, ssn, id, password;
	fin >> name; 
	fin >> ssn;
	fin >> id;
	fin >> password;
	join->requestJoin(name,  ssn,id,  password);
}
void JoinUI::showMessage()
{
	cout << "회원가입 완료" << endl;
}
void ResignUI::showMessage()
{
	cout << "회원탈퇴 완료" << endl;
}