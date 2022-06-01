#ifndef _ERR_
#define _ERR_

/* Print system call error message and terminate.
 * Uses errno to identify the error type. */
extern void syserr(const char *fmt, ...);

/* Print error message and terminate. */
extern void fatal(const char *fmt, ...);

#endif
