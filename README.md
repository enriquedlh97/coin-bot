# coin-bot
Slack bot to flip coins.

```
Pending:

Deployment.
Dockerization, etc.
General documentation of how it works.
```

## Initial Dev Setup

### Create Environment
Before creating the environment you will need to install:
- [`poetry`](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
- `python = "^3.10"`

Once you have poetry installed, go to the root of the repository and make sure
you have an appropriate python version active (`python = "^3.10"`). You can use
[`pyenv`](https://realpython.com/intro-to-pyenv/) or
[`conda`](https://docs.conda.io/en/latest/miniconda.html) for this.

#### Using Pyenv
If you are using `pyenv`, first install the specific python version by running:
```bash
pyenv install 3.10.3
```

Then set it as either the global or local version by running:

For setting as global:
```bash
pyenv global 3.10.3
```

For setting as global:
```bash
pyenv local 3.10.3
```

Then, depending on your poetry setup and previous python installations, it may
be necessary to explicitly declare the python version that `poetry` should use.
You can do this by getting the path to the executable by running:
```bash
pyenv which python
```
You can then paste the path to the python executable and run the following
command to tell poetry the python version to be used:
```bash
poetry en use <path-to-python-executable>
```

If you want to do everything with a single command you can just run:
```bash
poetry env use $(pyenv which python)
```

Finally, you can run the following to create a shell session:
```bash
poetry shell
```

#### Using Conda
If you are using `conda`, first create an environment with the specific python
version, for example:
```bash
conda create -n python3103 python=3.10.3
```

Then, depending on your poetry setup and previous python installations, it may
be necessary to explicitly declare the python version that `poetry` should use.
You can do this by activating your environment and getting the path to the
python executable.

Activate your environment (In this case the environment name is `python3103`):
```bash
conda activate python3103
```

Gte the path to the executable by running the following:
```bash
conda run which python
```

You can then paste the path to the python executable and run the following
command to tell poetry the python version to be used:
```bash
poetry en use <path-to-python-executable>
```

If you want to do everything together you can just run:
```bash
conda activate python3103
poetry env use $(conda run which python)
```

Finally, you can run the following to create a shell session:
```bash
poetry shell
```

### Installing Dependencies
To install all the required dependencies run:
```bash
poetry install
```

### Install `pre-commit`
```bash
poetry shell
pre-commit install
```

## Setup the environment variables
Create a file named `.env` within the `coin-bot/coinbot/` directory with the
following content (Make sure you edit the file before saving it):
```bash
ENV_STATE="dev" # or "stage" or "prod"

SLACK_TOKEN=<your-slack-token>
SLACK_EVENTS_TOKEN=<your-slack-events-token>

DEV_HOST="0.0.0.0"
STAGE_HOST=""
PROD_HOST=""

DEV_PORT=3000
STAGE_PORT=<stage-port>
PROD_PORT=<prod-port>
```

Make sure that:
- The value for `ENV_STATE` is a string wrapped in `""`.
- The values for all the hosts are strings wrapped in `""`,
- The values for the ports are integers (do not wrap them in `""`).

The values for the slack tokens can be pasted without being wrapped by `""`.
For more information about where to get the slack tokens see
[this](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04).

## Testing

### Testing with local execution
To simply test by locally running the slackbot without using the flask app run:
```bash
python coinbot/coinbot_test.py
```

You can check the channel to view the actions that the bot performed.

### Testing with Flask App
To test by locally running the flask app you will need to forward the port from
your personal firewall to the port that will be running on your workstation.
We sue port `3000`.

#### Setup Public URL
You can see more information [here](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04#step-5-mdash-creating-a-flask-application-to-run-your-slackbot)
about how to setup port forwarding.

A faster and easier approach is to use [`ngrok`](https://ngrok.com/). You will
need to create a free account. You can view more information [here](https://slack.dev/node-slack-sdk/tutorials/local-development)
about how to setup slack to use `ngrok`.

You will need to run:
```bash
ngrok http 3000
```

And configure the generated URL to be sued by slack. See more information
[here](https://slack.dev/node-slack-sdk/tutorials/local-development) and
[here](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04#step-5-mdash-creating-a-flask-application-to-run-your-slackbot).

### Run the Flask App and Test
Once you completed the previous step and the public URL is up, start the app
by running:
```bash
python coinbot/app.py
```

To verify that your app is up, open a new terminal window and curl the IP
address of your server (the one generated by `ngrok`) with the correct port at
`/slack/events`:
```bash
curl http://<YOUR-IP-ADDRESS>:3000/slack/events
```
That should return the following:
```bash
These are not the slackbots you're looking for.
```

Receiving the message `These are not the slackbots you're looking for.`,
indicates that your app is up and running.

After that, finish following the steps found [here](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04#step-5-mdash-creating-a-flask-application-to-run-your-slackbot)
to fully configure the slackbot in the Slack UI.

Once that is ready you can go back to the channel that you installed `CoinBot`
into and send a message containing the phrase `Hey Sammy, Flip a coin` in it.
Your bot will flip a coin and reply with the results.
