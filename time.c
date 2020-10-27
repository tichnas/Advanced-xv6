#include "types.h"
#include "stat.h"
#include "user.h"

int
main(int argc, char *argv[]) {
  int pid = fork();

  if (pid < 0) {
    printf(2, "Fork Failed\n");
  } else if (pid) {
    int wtime = -25;
    int rtime = -74;
    int status = waitx(&wtime, &rtime);
    printf(1, "%s ended with status %d\nWaiting time: %d\nRunning time: %d\n", argc == 1 ? "Default program" : argv[1], status, wtime, rtime);
  } else {
    if (argc == 1) {
      printf(1, "No program given. Running a default program...\n");
      for (volatile long long i = 0; i < 5e7; i++);
    } else {
      if (exec(argv[1], argv + 1) < 0)
        printf(2, "Exec Failed\n");
    }
  }

  exit();
}