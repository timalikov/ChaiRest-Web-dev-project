import { Component, Input } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  public email?: any;
  public password?: any;
  public errorMessage?: string;

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    this.authService.login(this.email!, this.password!).subscribe(() => {
        this.router.navigate(['/home']);
      },
      (error) => {
        this.errorMessage = "Wrong email or password";
      }
    );
  }
}
