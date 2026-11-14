/* TabuCol k-coloring local search.  usage: tabucol edges.txt n k maxiter seed
   edges.txt: lines "a b" (0-based). Prints "FOUND" and conflict-free coloring, or best conflicts. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage\n"); return 1; }
  FILE *f = fopen(argv[1], "r"); int n = atoi(argv[2]), k = atoi(argv[3]);
  long maxit = atol(argv[4]); srand(atoi(argv[5]));
  int cap = 1 << 20, m = 0; int *ea = malloc(cap * sizeof(int)), *eb = malloc(cap * sizeof(int));
  int a, b; while (fscanf(f, "%d %d", &a, &b) == 2) { if (m == cap) { cap *= 2; ea = realloc(ea, cap*sizeof(int)); eb = realloc(eb, cap*sizeof(int)); } ea[m] = a; eb[m] = b; m++; }
  int *deg = calloc(n, sizeof(int)); for (int i = 0; i < m; i++) { deg[ea[i]]++; deg[eb[i]]++; }
  int **adj = malloc(n * sizeof(int*)); int *fill = calloc(n, sizeof(int));
  for (int v = 0; v < n; v++) adj[v] = malloc((deg[v] + 1) * sizeof(int));
  for (int i = 0; i < m; i++) { adj[ea[i]][fill[ea[i]]++] = eb[i]; adj[eb[i]][fill[eb[i]]++] = ea[i]; }
  int *col = malloc(n * sizeof(int)); for (int v = 0; v < n; v++) col[v] = rand() % k;
  int *gam = calloc((size_t)n * k, sizeof(int)); /* gam[v*k+c] = #neighbors of v with color c */
  for (int v = 0; v < n; v++) for (int j = 0; j < deg[v]; j++) gam[v*k + col[adj[v][j]]]++;
  long *tabu = calloc((size_t)n * k, sizeof(long));
  long conf = 0; for (int i = 0; i < m; i++) if (col[ea[i]] == col[eb[i]]) conf++;
  long best = conf; int *bestcol = malloc(n * sizeof(int)); memcpy(bestcol, col, n*sizeof(int));
  for (long it = 0; it < maxit && conf > 0; it++) {
    int bv = -1, bc = -1, bd = 1 << 30, cnt = 0;
    for (int v = 0; v < n; v++) {
      if (gam[v*k + col[v]] == 0) continue;
      for (int c = 0; c < k; c++) if (c != col[v]) {
        int d = gam[v*k + c] - gam[v*k + col[v]];
        if (tabu[v*k + c] > it && conf + d >= best) continue;
        if (d < bd) { bd = d; bv = v; bc = c; cnt = 1; }
        else if (d == bd && rand() % (++cnt) == 0) { bv = v; bc = c; }
      }
    }
    if (bv < 0) continue;
    int old = col[bv]; col[bv] = bc; conf += bd;
    for (int j = 0; j < deg[bv]; j++) { int u = adj[bv][j]; gam[u*k + old]--; gam[u*k + bc]++; }
    tabu[bv*k + old] = it + 10 + (long)(0.6 * conf) + rand() % 10;
    if (conf < best) { best = conf; memcpy(bestcol, col, n*sizeof(int)); }
  }
  if (best == 0) { printf("FOUND\n"); for (int v = 0; v < n; v++) printf("%d\n", bestcol[v]); }
  else printf("BEST %ld\n", best);
  return 0;
}
