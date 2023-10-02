#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <wait.h>

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}


/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t child;
	int i = 5;

	while (i)
	{
		child = fork();
		if (child > 0)
		{
			printf("Zombie process created, PID: %d\n", child);
			sleep(2);
			i--;
		}
		else
			exit(0);
	}
	infinite_while();

}
