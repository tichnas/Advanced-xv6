#include "types.h"
#include "stat.h"
#include "user.h"

int
main(int argc, char *argv[]) {
  if (argc != 3) {
    printf(2, "Invalid arguments\n");
    exit();
  }

  int priority = atoi(argv[1]);
  int pid = atoi(argv[2]);

  int old_priority = set_priority(priority, pid);

  if (old_priority < 0) {
    printf(2, "Error setting priority\n");
  } else {
    printf(1, "Priority of PID %d updated from %d to %d\n", pid, old_priority, priority);
  }

  exit();
}