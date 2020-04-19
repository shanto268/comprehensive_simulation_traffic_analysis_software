"""
@author: sshanto
@date: 04/13/2020

Description:

Observations: 300 discrete states. Each state either AV, HV or empty.  

Actions: 2 actions. Switch lane or stay in lane.

Rewards: R1 - t_sim
    > R1 = aggregate reward function based on actions
    > t_sim = total timesteps needed to complete 10 cycles
    
Rendering: graphics and sim of each episode

state space is represented by: (agent_row, agent_col)
"""

