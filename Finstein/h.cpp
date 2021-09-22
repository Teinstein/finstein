#include <iostream>
using namespace std;
int i,n;

class student
{
    int marks[50];
    int roll[50];
    int rollno;
    int studmark;
    string name;
    string stdname[50];


public:
    void getdata();
    void showdata();
    void searchdata();
    void rollsort();
    void searchname();
    void display();
};
void student::getdata()
{
    for(i=0;i<n;i++)
    {
        cout<<"\n Information of student no "<<(i+1);
        cout<<"\n Enter Student name : ";
        cin>>name;
        cout << "\n Enter student roll no : ";
        cin >> rollno;
        cout << "\n Enter student marks: ";
        cin >> studmark;
        stdname[i]=name;
        roll[i]=rollno;
        marks[i]=studmark;
    }
}
void student::showdata()
{
    for(i=0;i<n;i++)
    {
        cout<<"\n Following are the details of student no.; "<< (i+1);
        cout<<"\n Name of Student is : "<<stdname[i];
        cout<<"\n Roll no of student is : "<<roll[i];
        cout<<"\n Marks of Student is :"<<marks[i];
        cout<<endl;


    }
    cout<<endl;
}
void student::searchdata()                                      //linear search
{
    int studentmarks;
    cout<<"\n enter marks  u want to search :";
    cin>>studentmarks;
    int i=0;
    bool  flag=true;

    while(i<n)
    {
        if (studentmarks == marks[i])
        {
            cout << "\n Student found!!";
            cout << "\n Name of Student is : " << name;
            cout << "\n Roll no of student is : " << rollno;
            cout << endl;

            flag = false;


        }
        if (flag) {
            cout << "\n NO DATA FOUND!!!";
        }

        i++;
    }

}
void student::rollsort()                                 //Bubble sort
{
    int temp;
    string tname;
    int tmarks;
    for(i=0;i<(n-1);i++)                                // for no of comparison
    {
        for(int j=0;j<((n-1)-i);j++)                    // for  no of iteration
        {
            if(roll[j]>roll[j+1])
            {
                temp=roll[j];                          //swapping
                roll[j]=roll[j+1];
                roll[j+1]=temp;

                tname=stdname[j];
               stdname [j]=stdname[j+1];
                stdname[j+1]=tname;

                tmarks=marks[j];
                marks [j]=marks[j+1];
                marks[j+1]=tmarks;

            }
        }
    }
    cout<<"\n Sorted Call List"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<roll[i]<<" "<<stdname[i]<<endl;
        cout<<endl;
    }
}
void student::searchname()             //binary search
{
    string key;
    cout<<"\n Enter name u wan to search";
    cin>>key;
    string swapname;
    for (i = 0; i < (n - 1); i++)                                // for no of comparison
    {
        for (int j = 0; j < ((n - 1) - i); j++)                    // for  no of iteration
        {
            if (stdname[j] > stdname[j + 1]) {
                swapname = stdname[j];                          //swapping
                stdname[j] = stdname[j + 1];
                stdname[j + 1] = swapname;

            }
        }
    }
    int start = 0,mid;
    int not_found=1;
    int end = n - 1;
    while (start <= end)
    {
        int mid=( start + end-1 )/ 2;

        // Check if x is present at mid
        if (stdname[mid]==key)
        {
            not_found = 0;
            
        }
        
        if(!(not_found)){
            cout << "Found! \n";
            cout << " ROLL NO:" << roll[mid] << "\n";
            cout << "NAME:" <<stdname[i] << "\n";
            cout << "SGPA:" << marks[mid] << "\n";
            break;
        }

        // If x greater, ignore left half
        if (stdname[mid]>key)
            start = mid + 1;

            // If x is smaller, ignore right half
        else
            end = mid - 1;

    }
    if (not_found) cout << "not found";

}

void  student :: display()
{
      string stdname[i];
      int roll[i];
      float marks[i];
    for (int i = 0; i < n; i++)
    {
     cout<<"\n  NAME : "<<stdname[i];
     cout<<"\n  ROLL NO : "<<roll[i];
        cout << "\n SGPA:" << marks[i];
    }
}




int main()
{
    cout<<"\n Enter no of students : ";
    cin>>n;
    student s1;
    s1.getdata();
    s1.showdata();
    s1.searchdata();
    s1.rollsort();
    s1.searchname();
    s1.display();
    return 0;

}