import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';
import { User } from '../models';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  public username?: string;
  public email?: string;
  public password?: string;
  errorMessage?: any;

  constructor(
    private authService: AuthService,
    private router: Router
  ) { }

  register(): void {
    this.authService.register(this.username!, this.password!, this.email!)
      .subscribe(
        response => {
          localStorage.setItem('token', response.access);
          this.router.navigate(['/login']);
        },
        error => console.error(error)
      );
  }
}
