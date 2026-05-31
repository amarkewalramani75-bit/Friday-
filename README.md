# Friday-
The mobile version of friday the ai of iron man on your mobile using free api from Google give it your touch and feel like Tony stark
graph TD
    subgraph Inputs
    A[Sensors/Mic/Camera] --> B[Event Bus]
    end

    subgraph Core
    B --> C{Decision Engine}
    C --> D[Cognitive Module]
    D --> E[Memory/Database]
    end

    subgraph Outputs
    C --> F[Hardware/Actuators]
    C --> G[Speech/Display]
    end

    subgraph Feedback
    F --> A
    end

