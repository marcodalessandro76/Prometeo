#ifndef SIMULATION_H
#define SIMULATION_H

class Simulation {
public:
    explicit Simulation(long long samples);
    void run();
    double getPiEstimate() const;

private:
    long long num_samples;
    double pi_estimate;
};

#endif // SIMULATION_H
