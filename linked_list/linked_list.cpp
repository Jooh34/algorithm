#include <stdio.h>

struct Node    //자료형을 정의합니다.
{
	int val;
	Node* next;
    Node (int _val, Node* _next) : val(_val), next(_next) {};
};

class linked_list
{
private:
    Node *head, *tail;
public:
    linked_list() {
        head = NULL;
        tail = NULL;
    }
    void add(int n) {
        if (head == NULL) {
            head = new Node(n, NULL);
            tail = head;
        }
        else {
            tail->next = new Node(n, NULL);
            tail = tail->next;
        }
    }
	void remove(int n) {
		Node *it = head;
		while(it->next != NULL) {
			if(it->next->val == n) {
				Node *temp = it->next;
				it->next = it->next->next;
				delete temp;
				break;
			}
			it = it->next;
		}
	}
    void printAll() {
        Node *it = head;
        while(it != NULL) {
            printf("%d\n", it->val);
            it = it->next;
        }
    }
    void reverseFrom(int n) {
		Node *it = head;
		while(it != NULL) {
			if(it->next->val == n) break;
			it = it->next;
		}
		if(it == NULL) return;

		Node *temp_tail = it;
		it = it->next;

		Node *prev = NULL;
		while(it != NULL) {
			Node *next = it->next;
			it->next = prev;
			prev = it;
			it = next;
		}

		temp_tail->next = prev;
    }
};

int main () {
    linked_list list = linked_list();
    list.add(1);
    list.add(2);
    list.add(3);
    list.add(4);
    list.add(5);
    list.add(6);
	list.reverseFrom(4);
	list.printAll();
}
