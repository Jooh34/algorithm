#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;
struct genre_info {
    string genre;
    vector<pair<int, int>> musics;

    genre_info(string _genre) : genre(_genre) {};
};

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;

    unordered_map<string, genre_info> m;

    int len = genres.size();
    for(int i=0; i<len; i++) {
        string g = genres[i];
        int p = plays[i];

        auto got = m.find(g);
        if (got == m.end()) { // not exist
            genre_info g_i(g);
            g_i.musics.push_back(make_pair(i,p));
            m.insert({g,g_i});
        }
        else { // exist
            got->second.musics.push_back(make_pair(i,p));
        }
    }

    vector<pair<string,int>> sum_list;

    for(auto it=m.begin(); it != m.end(); it++) {
        genre_info &g_i = it->second;


        // cal sum and push list
        int sum = 0;
        for (auto music : g_i.musics) {
            sum += music.second;
        }
        sum_list.push_back(make_pair(g_i.genre, sum));

        // sort musics
        sort(g_i.musics.begin(), g_i.musics.end(),
            [](const pair<int, int> &l, const pair<int, int> &r){
                return l.second > r.second;
            });
    }

    // sort sum_list
    sort(sum_list.begin(), sum_list.end(),
        [](const pair<string, int> &l, const pair<string, int> &r) {
            return l.second > r.second;
        });

    for (auto it=sum_list.begin(); it != sum_list.end(); it++) {
        string genre = it->first;
        auto got = m.find(genre);
        if(got->second.musics.size() >= 2) {
            answer.push_back(got->second.musics[0].first);
            answer.push_back(got->second.musics[1].first);
        }
        else {
            answer.push_back(got->second.musics[0].first);
        }
    }
    return answer;
}

int main () {
    vector<string> genres{"classic", "pop", "classic", "classic", "pop"};
    vector<int> plays{500, 600, 150, 800, 2500};

    vector<int> answer = solution(genres, plays);
    for (int a : answer) {
        cout << a << endl;
    }
}
