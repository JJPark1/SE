#include <string>
#include "boundary.h"
ifstream fin;

JoinUI::JoinUI(Join* j) :join(j) {}

void JoinUI::join_function()
{ // �ٿ����

	string name, ssn, id, password;
	fin >> name; 
	fin >> ssn;
	fin >> id;
	fin >> password;
	join->requestJoin(name,  ssn,id,  password);
}
void JoinUI::showMessage()
{
	cout << "ȸ������ �Ϸ�" << endl;
}
void ResignUI::showMessage()
{
	cout << "ȸ��Ż�� �Ϸ�" << endl;
}