#include <string>
#include "control.h"
#include "boundary.h"

void Join::requestJoin(string name,string ssn,string id,string password)
{ // ��Ʈ��
	UserDetail* userDetail;
	string n = name;
	string s = ssn;
	string i = id;
	string p = password;
	user->addUser(userDetail); // ���� �߰�
	userDetail->addtoUser(n,s,i,p);
	joinUI->showMessage();


}
void Login::requestLogin()
{

}
void Logout::requestLogout()
{

}
void Resign::requestResign()
{

}