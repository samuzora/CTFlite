# CTF-cord

A Discord bot for all your CTF management needs. 

## Features

* CTF management
	* CTF details pulled from CTFtime and converted into an embed
	* Private channels, scheduled events and team roles automatically created
	* Score and challenge solves tracking
	* Supports non-CTFtime CTFs too!

* Weekly sends upcoming CTFs on CTFtime

## Documentation

### /ctf

#### `/ctf details <ctftime_link>`

> View details about a CTF 

##### Parameters:

* `ctftime_link: str`
	* Link to the CTF on CTFtime, can also be the 4-digit ID of the CTF (the last 4 digits in the CTFtime link)

#### `/ctf signup <team_name> <ctftime_link:optional> <userX:optional>`

> Register for a CTF and let the bot handle the rest. This will create a channel designated for that CTF. All CTF-related commands must be used in that channel. 

##### Parameters:

* `team_name: str`
	* Your team's name for that CTF, used to create roles for the team
* `ctftime_link: str = ''`
	* Link to the CTF on CTFtime, can also be the 4-digit ID of the CTF. If left blank, a custom CTF (not based on CTFtime) can be created
* `users1-4`: discord.User = None
	* Can be used to add users to your team. Currently, up to a maximum of 5 members inclusive of yourself can be added to a team

##### `/ctf unsignup`

> Un-register for a CTF. All bot-created channels, events etc. will be cleared.

*Must be invoked from the designated CTF channel*

### /chall

#### `/chall solved <chall_name> <chall_points:optional>`

> Mark a challenge as solved and optionally specify the number of points the challenge has.

##### Parameters:

* `chall_name: str`
	* Name of the challenge
* `chall_points: int = 0`
	* Challenge score, can be omitted

#### `/chall solving <chall_category> <chall_name>`

> Create a thread for the challenge.

##### Parameters:
* `chall_category: str`
	* Challenge category, used to create thread for the challenge
* `chall_name: str`
	* Challenge name, used to create thread for the challenge

### /settings

> Configuration for bot
