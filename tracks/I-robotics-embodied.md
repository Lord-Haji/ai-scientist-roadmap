# Track I: Robotics and Embodied AI (optional)

**You become:** someone building robot learning and vision-language-action (VLA) policies. This track is adapted from the robotics block of [leviance/AI-Research-Curriculum](https://github.com/leviance/AI-Research-Curriculum) and is optional unless physical AI is your goal.  
**Requires:** Levels 2, 4, 6A, 6B (Track C and E help). **Time:** 600-900 h (long).

## Sequence

| Step | Course | Notes |
|---|---|---|
| 1 | Differential equations and mechanics bridge: selected [MIT 18.03SC](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) + mechanics | ODEs, state space, numerical integration. |
| 2 | [Modern Robotics (Northwestern)](https://modernrobotics.northwestern.edu/) | Frames, SO(3)/SE(3), kinematics, dynamics, planning, control. |
| 3 | [MIT Underactuated Robotics](https://underactuated.mit.edu/) | LQR, trajectory optimization, MPC, policy search. |
| 4 | [MIT Robotic Manipulation](https://manipulation.csail.mit.edu/Fall2025/) | Perception, grasping, planning, manipulation stacks (Drake). |
| 5 | [Stanford CS224R Deep RL / robot learning](https://cs224r.stanford.edu/) and [Berkeley CS285](https://rail.eecs.berkeley.edu/deeprlcourse/) | BC, DAgger, offline RL, model-based, goal-conditioned. |
| 6 | Embodied foundation models practicum (below) | Paper- and code-driven. |

## VLA practicum resources

[Open X-Embodiment](https://github.com/google-deepmind/open_x_embodiment), [OpenVLA](https://arxiv.org/abs/2406.09246), [Physical Intelligence openpi](https://github.com/Physical-Intelligence/openpi), pi0 (2410.24164), pi0.5 (2504.16054), RT-2 (2307.15818), Open X-Embodiment paper (2310.08864), Gemini Robotics. Simulators: MuJoCo, ManiSkill, LIBERO, Isaac.

## Papers

DAgger (1011.0686); World Models (1803.10122); RT-2; Open X-Embodiment; OpenVLA; pi0; pi0.5; plus action-chunking/diffusion-policy papers.

## Projects

Dynamics simulator; robot kinematics + RRT planner; control lab (swing-up, LQR, MPC); simulated pick-and-place stack with recovery; progressive robot learning study (classical vs BC vs RL vs generative policy); a mini-VLA with a simple action head and a flow-matching head, evaluated on generalization splits, with a 6-10 page report.

## Done when

You can describe and build the full loop from camera pixels and language to actions on a simulated robot, and evaluate generalization honestly.
