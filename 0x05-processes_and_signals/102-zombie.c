#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>


/**
 * infinite_while - a infinite while loop
 *
 * Return: status code
 */
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - a function to create zombie process
 *
 * Return: 0 always
 */
int main(void)
{
	int num = 0;
	pid_t pid;

	while (num < 5)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			_exit(EXIT_SUCCESS);
		}
		num += 1;
	}
	infinite_while();

	return (0);
}
