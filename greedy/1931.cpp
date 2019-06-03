#include <cstdio>
#include <algorithm>

using namespace std;

class Meeting{
public:
    int start;
    int end;
    Meeting(){

    }
    Meeting(int start, int end){
        this->start = start;
        this->end = end;
    }
};

bool operator <(Meeting const &a, Meeting const &b){
    return a.end < b.end;
}

Meeting meeting[100000];

int main () {
  int T;
  scanf("%d",&T);

  for(int i=0; i<T; i++) {
    scanf("%d %d",&meeting[i].start,&meeting[i].end);
  }
  std::sort(meeting, meeting+T);

  int count = 0;
  int current = 0;
  for (int i=0; i<T; i++) {
    int start = meeting[i].start;
    int end = meeting[i].end;
    if (current <= start) {
      count++;
      current = end;
    }
  }

  printf("%d\n", count);
}
