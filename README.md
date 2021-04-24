# tgdsmells

## Helper classes for the Team Group Data Sharing Medium & Electronic Local Link System

Learn more about [TGDSMELLS](https://github.com/RLBot/RLBot/wiki/Team-Match-Communication-Protocol).

## Upgrading from TMCP

Upgrading from TMCP to TGDSMELLS is simple. All you need to do is replace `tmcp` with `tgdsmells` in your requirements.txt, then replace `from tmcp import` with `from tgdsmells import`.

---

## How to use

Start by creating an instance of the TGDSMELLSHandler.
You should pass in your agent.

```py
from tgdsmells import TGDSMELLSHandler

class MyBot(BaseAgent):
    def initialize_agent(self):
        self.tgdsmells_handler = TGDSMELLSHandler(self)
```

Usage is also very straightforward:

```py
from tgdsmells import TGDSMELLSMessage, ActionType

...
    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        # Receive and parse all new matchcomms messages into TGDSMELLSMessage objects.
        new_messages: List[TGDSMELLSMessage] = self.tgdsmells_handler.recv()
        # Handle TGDSMELLSMessages.
        for message in new_messages:
            if message.action_type == ActionType.BALL:
                print(message.time)
        
        ...

        # You can send messages like this.
        self.tgdsmells_handler.send_boost_action(pad_index)

        # Or you can create them and send them more directly:
        my_message = TGDSMELLSMessage.ball_action(self.team, self.index, estimated_time_of_arrival)
        self.tgdsmells_handler.send(my_message)
```

The handler will throttle your messages if you send them too quickly.
If you want to make sure all of your messages are sent, you can create a backlog like this:

```py
# During initialization, create a backlog list.
self.backlog = []

...
# Sending returns false if a message was not sent.
if not self.tgdsmells_handler.send(message):
    self.backlog.append(message)

...
# In your main loop, check whether you have any messages in the backlog.
if self.backlog:
    backlog_message = self.backlog.pop(0)
    # Try sending the message again. If it doesn't work, return it to the backlog.
    if not self.tgdsmells_handler.send(backlog_message):
        self.backlog.insert(0, backlog_message)
```

## Avoiding major breaking changes

This package is regularly updated according to the latest TGDSMELLS specification.
To avoid your bot breaking during tournaments due to major version updates, you can use a virtual_environment and pin a specific version of this package.

In your requirements.txt:

```txt
tgdsmells==1.*
```

In your bot.cfg:

```toml
[Locations]
use_virtual_environment = true
requirements_file = ./requirements.txt
```

If you don't want to do this, you can also disable the handler if a different version of the package is used.
This will not send or receive any messages, but will pretend as if it was sending all and receiving none.

```py
from tgdsmells import TGDSMELLS_VERSION

if TGDSMELLS_VERSION[0] != 1:
    my_handler.disable()
```
