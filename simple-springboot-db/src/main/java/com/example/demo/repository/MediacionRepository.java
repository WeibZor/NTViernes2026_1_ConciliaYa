package com.example.demo.repository;

import com.example.demo.model.Mediacion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MediacionRepository extends JpaRepository<Mediacion, Long> {
}
