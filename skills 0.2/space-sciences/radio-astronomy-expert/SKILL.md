---
name: radio-astronomy-expert
version: 1.0.0
description: Expert-level radio astronomy covering radio telescopes, interferometry, VLBI, radio sources, pulsar timing, spectral line observations, and radio transients.
author: luokai25
tags: [radio astronomy, interferometry, VLBI, pulsars, spectral lines, radio telescopes]
---

# Radio Astronomy Expert

## Before Starting
1. Which frequency band? (cm, mm, sub-mm)
2. Continuum or spectral line?
3. Single dish or interferometry?

## Core Expertise Areas

### Radio Telescopes
Single dish: large collecting area, limited resolution by diffraction limit.
Parabolic reflector: focuses radio waves to receiver at prime or secondary focus.
FAST: 500m dish in China, most sensitive single dish in the world.
Receiver systems: LNA amplifiers, mixers, spectrometers, cryogenic cooling.
System temperature: receiver noise plus sky background limits sensitivity.

### Radio Interferometry
Baseline: separation between two antennas, determines angular resolution.
Visibility: complex number measured by each baseline, Fourier transform of sky.
UV plane: spatial frequency coverage, determines image quality.
Aperture synthesis: Earth rotation fills UV plane over time.
CLEAN algorithm: iterative deconvolution of dirty beam from dirty image.

### VLBI
Very long baseline interferometry: intercontinental baselines, microarcsecond resolution.
Atomic clocks: GPS and hydrogen masers synchronize stations.
EHT: global VLBI at 1.3mm, imaged black hole shadows.
Space VLBI: RadioAstron satellite extended baselines beyond Earth diameter.

### Radio Sources
Pulsars: rotating neutron stars, stable rotation used as clocks.
Pulsar timing arrays: gravitational wave background detection.
FRBs: fast radio bursts, millisecond transients, largely extragalactic.
HI 21cm line: neutral hydrogen spin-flip transition, traces galaxy structure.
Molecular lines: CO, OH, NH3 probe cold gas in star-forming regions.

## Best Practices
- Always check for radio frequency interference before analysis
- Calibrate amplitude and phase with known calibrator sources
- Apply proper motion and parallax corrections for astrometry
- Assess image dynamic range and sensitivity limits

## Common Pitfalls
| Pitfall | Fix |
|---|---|
| RFI contamination | Flag affected data before imaging |
| Insufficient UV coverage | Observe at multiple hour angles or add more antennas |
| CLEAN divergence | Use appropriate CLEAN depth and mask |
| Confusing flux density and luminosity | Always specify distance if quoting luminosity |

## Related Skills
- astrophysics-expert
- physics/electromagnetism-expert
- signal-processing within engineering |
