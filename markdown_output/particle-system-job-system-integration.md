---
title: "Particle System C# Job System integration"
category: "General"
source_file: "particle-system-job-system-integration.html"
doc_type: "manual"
---

# Particle System C# Job System integration

A **Particle System** can use Unity’s C# Job System to apply custom behaviors to particles.

Unity distributes work from the C# Job System across worker threads, and can make use of the Burst Compiler. The GetParticles() and SetParticles() methods offer similar functionality, but run on the main thread and cannot make use of Unity’s Burst Compiler. 

By default, a Particle System job only has access to one or more particles belonging to that Particle System. Unity passes this data to the job using a ParticleSystemJobData struct. You must pass any other data that the job requires as additional parameters.

To access particle data, Unity supports the following job types:

## IJobParticleSystem

This job type executes a single job on a single worker thread. The job has access to every particle belonging to the Particle System. For example code on this job type, see the IJobParticleSystem.Execute() Scripting reference.

## IJobParticleSystemParallelFor

This job type executes multiple jobs across multiple worker threads. Each job can only access the particle at the index specified by the job’s Execute() function. For example code on this job type, see the IJobParticleSystemParallelFor.Execute() Scripting reference.

## IJobParticleSystemParallelForBatch

This job type executes multiple jobs across multiple worker threads. Each job can only access the particles within the range specified by the job’s Execute() function. For example code on this job type, see the IJobParticleSystemParallelForBatch.Execute() Scripting reference.

## Burst

As with any other C# job, you can use the Burst Compiler to compile your particle jobs into highly optimized Burst jobs. For more information, see the Burst Compiler documentation.

New feature in Unity 2019.3