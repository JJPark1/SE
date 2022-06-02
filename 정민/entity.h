#pragma once
#include <iostream>
using namespace std;

class System
{
public:
	void systemLogin();
	void removeAuthority();
	void systemLogout();
	//void requestLogout();
};
class UserDetail
{
	string name, ssn, password, id;
public:
	bool isValid(string name, string ssn, string id, string password);
	void addtoUser(string name, string ssn, string id, string password);
	void deletetoUser();
};
struct UserNode {
	UserDetail* userDetail;
	struct UserNode* link;
};

class User {
	UserNode* head;
	UserDetail* selectedUser;
public:
	void addUser(UserDetail* userDetail);
	void deleteUser(string ID);
	bool searchUser(string ID);
	UserDetail* getSelectedUser();
};
