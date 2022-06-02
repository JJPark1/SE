#include "boundary.h"
#include "control.h"
#include <fstream>
#include <string>
ifstream fin;
ofstream fout;
using namespace std;

#define INPUT_FILE_NAME "input.txt"
#define OUTPUT_FILE_NAME "output.txt"
void doTask();

//FILE* in_fp, * out_fp;



//
//
//void User::addUser(string _name, string _ssn, string _id, string _password)
//{
//    name = _name;
//    ssn = _ssn;
//    id = _id;
//    password = _password;
//}
//bool User::isValid(string _id, string _password)
//{
//    //cout << "입력 한거: " << _id << "  " << _password << endl;*/
//
//    if (this->id == _id && this->password == _password)
//    {
//
//
//        return true;
//    }
//    else
//        return false;
//}
//void User::deleteUser()
//{
//    name = "";
//    ssn = "";
//    id = "";
//    password = "";
//    cout << "resign complete" << endl;
//}

int main()
{	// 파일 입출력을 위한 초기화
    //FILE* in_fp = fopen(INPUT_FILE_NAME, "r+");


  //  in_fp.open("input.txt");


    //FILE* out_fp = fopen(OUTPUT_FILE_NAME, "w+");


    fin.open(INPUT_FILE_NAME);
    fout.open(OUTPUT_FILE_NAME);
    doTask();
    return 0;
}

void doTask()
{
    // 메뉴 파싱을 위한 level 구분을 위한 변수
    string menu_level_1 , menu_level_2;
    char is_program_exit = 0;

  

    int count = 1;
   while (!is_program_exit)
   {
 
        
        // 입력파일에서 메뉴 숫자 2개를 읽기

       fin >> menu_level_1; fin >> menu_level_2;
        
        int menu_level_1_ = stoi(menu_level_1);
        int menu_level_2_ = stoi(menu_level_2);
       // cout << "menu 1,2= " << menu_level_1_ << "  " << menu_level_2_ << endl;
        
        // 메뉴 구분 및 해당 연산 수행
        if (menu_level_1_ == 1)
        {
            if (menu_level_2_ == 1)
            {
                cout << endl << "join" << endl;
                join();
            }

            else if (menu_level_2_ == 2)
            {
                cout << endl << "resign" << endl;
                resign();

            }
        }
        else if (menu_level_1_ == 2)
        {
            if (menu_level_2_ == 1)
            {
                cout << endl << "login" << endl;
                login();
            }
        }
        else if (menu_level_1_ == 6)
        {
            if (menu_level_2_ == 1)
            {
                //show1();
                cout << endl << "exit" << endl;
                program_exit();
                is_program_exit == 1;
                break;
            }
        }
      
       
        if(is_program_exit==1)
        return;
        count++;
      

    }

}
void join()
{


    string NAME, SSN, ID, PASSWORD;
    //    // 입력 형식 : 이름, 주민번호, ID, Password를 파일로부터 읽음
    in_fp >> NAME >> SSN >> ID >> PASSWORD;

    
    //    // 해당 기능 수행  
    person[user_number++].addUser(NAME, SSN, ID, PASSWORD);

 
    //        // 출력 형식
    //    //fprintf(out_fp, "1.1. 회원가입\n");
    //   // fprintf(out_fp, "%s %s %s %s\n", name, SSN, ID, password);
}
void login()
{

    string id, pw;
    in_fp >> id >> pw;
    bool tryLogin = true;
    for (int i = 0; i < 10; i++)
    {
        if (person[i].isValid(id, pw))
        {
            cout << "로그인 성공" << endl;
            tryLogin = true;
            break;
        }
        else
        {
            tryLogin = false;

        }
    }

    
    if (tryLogin == false  )
    {
        cout << "로그인 실패" << endl;
   }
}
void resign()
{
    person[--user_number].deleteUser();
}
void logout()
{
    cout << "logout()" << endl;
}
void program_exit()
{
 
}
