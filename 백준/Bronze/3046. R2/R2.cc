/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 3046                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: choigaon1028_cpp <boj.kr/u/choigaon1028_c   +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/3046                           #+#        #+#      #+#    */
/*   Solved: 2026/01/03 23:09:08 by choigaon1028_c###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <iostream>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int R1, S;
    cin >> R1 >> S;
    cout << 2 * S - R1 << "\n";
    return 0;
}